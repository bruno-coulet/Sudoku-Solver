import os, statistics
from SolverBacktracking.Backtracking import Backtracking
from SolverBruteForce.BruteForce import BruteForce

class Testing:
    '''Tests either brute force or backtracking'''
    def __init__(self):

        self.algorithm_name = input('\nQuelle méthode voulez-vous utiliser, "bruteforce" ou "backtracking" : ')
        if self.algorithm_name.lower() == 'bruteforce':
            self.solver = BruteForce()
        elif self.algorithm_name.lower() == 'backtracking':
            self.solver = Backtracking()
        else:
            raise ValueError("Méthode invalide. Veuillez choisir 'BruteForce' ou 'Backtracking'.")

         

    def run_tests(self):
        input_folder = "input"
        grid_names = [file for file in os.listdir(input_folder) if file.endswith(".txt")]

        # Creates the markdown table
        table = "| Fichier testé | Grille testée | Temps d'exécution  |\n"
        table += "| -------------- | ------------- | ----------------- |\n"

        # Initialize variables for calculating min, max, and average time
        execution_times = []

        for grid_name in grid_names:
            print(f"\nTesting de {grid_name}...")
            file_path = os.path.join(input_folder, grid_name)
            elapsed_time = self.solver.begin(file_path)

            # Update table with current execution stats
            table += f"| {self.algorithm_name}  |  {grid_name}   | {(elapsed_time * 1000):.3f} ms |\n"
                        
            if elapsed_time is not None:
                execution_times.append(elapsed_time)

            # if None:
            #     print(f"Pas de solution trouvée pour {grid_name}.\n")
                
        if execution_times:
            # Calculate min, max, and average times
            minimum_time = min(execution_times)
            maximum_time = max(execution_times)
            average_time = statistics.mean(execution_times)

            # Update the markdown table with the final results
            table += f"\nTemps le plus court : {(minimum_time * 1000):.3f} ms\n"
            table += f"Temps le plus long : {(maximum_time * 1000):.3f} ms\n"
            table += f"Temps moyen : {(average_time * 1000):.3f} ms\n"

        print(table)
        return table


if __name__ == "__main__":
    test = Testing()
    table = test.run_tests()

   # creates README.md to store the table
    try:
        with open("README.md", "w") as readme_file:
            readme_file.write(table)
        print("Le fichier README.md a été créé avec succès.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la création du fichier README.md : {e}")