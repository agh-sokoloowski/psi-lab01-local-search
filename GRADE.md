Dear Student,

I regret to inform you that you've received only **21** out of 50 points for this assignment.\
There still exist some issues that should be addressed before the deadline (2021-11-21 22:00:00 GMT). For further details, please refer to the following list:

<details><summary>Kempe chain should have result with no conflicts &gt;&gt; there are still 4 conflicts after kempe chain</summary>	- bad edges: [0, 4, 0, 0, 0, 0, 0, 0, 0]<br>	- state: (0: 1) (1: 0) (2: 0) (3: 0) (4: 1) (5: 1) (6: 1) (7: 1) (8: 2)<br>	- graph: {0: {8, 4, 5}, 1: {4, 6}, 2: {4, 5}, 3: {6}, 4: {0, 1, 2}, 5: {0, 2}, 6: {1, 3}, 7: {8}, 8: {0, 7}}</details>
<details><summary>Kempe chain should have result with no conflicts &gt;&gt; there are still 2 conflicts after kempe chain</summary>	- bad edges: [0, 0, 2, 0, 0, 0, 0, 0, 0]<br>	- state: (0: 2) (1: 0) (2: 0) (3: 0) (4: 1) (5: 1) (6: 1) (7: 1) (8: 2)<br>	- graph: {0: {8, 4, 5}, 1: {4, 6}, 2: {4, 5}, 3: {6}, 4: {0, 1, 2}, 5: {0, 2}, 6: {1, 3}, 7: {8}, 8: {0, 7}}</details>
<details><summary>Kempe chain should solve direct conflicts &gt;&gt; kempe chain fails to correctly fix direct coloring conflict</summary>	- state: (0: 1) (1: 0) (2: 0) (3: 0) (4: 1) (5: 1) (6: 1) (7: 1) (8: 2)<br>	- graph: {0: {8, 4, 5}, 1: {4, 6}, 2: {4, 5}, 3: {6}, 4: {0, 1, 2}, 5: {0, 2}, 6: {1, 3}, 7: {8}, 8: {0, 7}}</details>
<details><summary>Kempe chain should solve direct conflicts &gt;&gt; kempe chain fails to correctly fix direct coloring conflict</summary>	- state: (0: 2) (1: 0) (2: 0) (3: 0) (4: 1) (5: 1) (6: 1) (7: 1) (8: 2)<br>	- graph: {0: {8, 4, 5}, 1: {4, 6}, 2: {4, 5}, 3: {6}, 4: {0, 1, 2}, 5: {0, 2}, 6: {1, 3}, 7: {8}, 8: {0, 7}}</details>
<details><summary>Kempe chain should solve indirect conflicts &gt;&gt; kempe chain fails to fix indirect coloring conflicts:</summary>	- state: (0: 1) (1: 0) (2: 0) (3: 0) (4: 1) (5: 1) (6: 1) (7: 1) (8: 2)<br>	- graph: {0: {8, 4, 5}, 1: {4, 6}, 2: {4, 5}, 3: {6}, 4: {0, 1, 2}, 5: {0, 2}, 6: {1, 3}, 7: {8}, 8: {0, 7}}</details>
<details><summary>Kempe chain should handle cycles &gt;&gt; kempe chain doesn&#x27;t handle correctly cycles in the graph</summary>	- state: (0: 1) (1: 0) (2: 0) (3: 0) (4: 1) (5: 1) (6: 1) (7: 1) (8: 2)<br>	- graph: {0: {8, 4, 5}, 1: {4, 6}, 2: {4, 5}, 3: {6}, 4: {0, 1, 2}, 5: {0, 2}, 6: {1, 3}, 7: {8}, 8: {0, 7}}</details>
<details><summary>Random choice hill climbing should find the random improving neighbor &gt;&gt; algorithm is deterministic, always returns the same state, while it should be random (goal type: GoalType.MIN))</summary></details>
<details><summary>Reheat should restore temp and reset schedule &gt;&gt; reheating modifies the state, it shouldn&#x27;t!</summary></details>
<details><summary>Update temperature not goes below min temperature &gt;&gt; update should be able to reach the minimal temperature</summary></details>
<details><summary>Update temperature updates cooling time &gt;&gt; expected update temperature to  update cooling time by 1,not by 0</summary></details>
<details><summary>Calculate transition probability &gt;&gt; expected to calculate 2.71828182845905for delta model improvement 1 amd temperature 1</summary></details>
<details><summary>Calculate transition probability &gt;&gt; expected to calculate 22026.4657948067for delta model improvement 10 amd temperature 1</summary></details>
<details><summary>Calculate transition probability &gt;&gt; expected to calculate 2.68811714181614e+43for delta model improvement 100 amd temperature 1</summary></details>
<details><summary>Calculate transition probability &gt;&gt; expected to calculate 1.97007111401705e+434for delta model improvement 1000 amd temperature 1</summary></details>
<details><summary>Find next state gets random neighbour &gt;&gt; Expected &#x27;_get_random_neighbours&#x27; to be called once. Called 0 times.</summary></details>
<details><summary>Find next state returns next state if state is better &gt;&gt; expected algorithm to select improving state</summary></details>
<details><summary>Find next state calculates transition probability if state is not better &gt;&gt; Expected &#x27;_calculate_transition_probability&#x27; to be called once. Called 0 times.</summary></details>
<details><summary>Find next state updates temperatures &gt;&gt; Expected &#x27;_update_temperature&#x27; to have been called once. Called 0 times.</summary></details>

-----------
I remain your faithful servant\
_Bobot_