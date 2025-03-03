/* 
 * Dream Interpreter Knowledge Base
 * Contains facts and rules about dream symbols and their interpretations
 */

/* Dream symbol definitions - symbol(Name, Context, Interpretation) */

/* Natural elements */
symbol(water, calm, "Represents peace and emotional clarity").
symbol(water, rough, "May indicate emotional turbulence or feeling overwhelmed").
symbol(water, rising, "Could symbolize rising emotions or feeling out of control").
symbol(water, _, "Represents your emotional state or unconscious mind").

symbol(fire, controlled, "Can represent passion, transformation, or desire").
symbol(fire, destructive, "May symbolize anger, destruction, or purification").
symbol(fire, warming, "Often indicates comfort, protection, or creative energy").
symbol(fire, _, "Represents transformation, passion, or destructive forces").

symbol(earth, _, "Connection to reality, stability, or groundedness").
symbol(wind, _, "Change, freedom, or direction in life").

/* Creatures */
symbol(snake, _, "Transformation, hidden fears, wisdom, or healing").
symbol(bird, flying, "Freedom, aspiration, or higher perspective").
symbol(bird, caged, "Feeling restricted or limited in your potential").
symbol(bird, _, "Freedom, perspective, or aspirations").
symbol(spider, _, "Creativity, patience, or feeling trapped").
symbol(dog, friendly, "Loyalty, companionship, or protection").
symbol(dog, aggressive, "Betrayal, fear, or conflict with friends").
symbol(dog, _, "Loyalty, friendship, or protection").
symbol(cat, _, "Independence, mystery, or intuition").

/* Objects */
symbol(house, familiar, "Representation of yourself or current state of mind").
symbol(house, unfamiliar, "Exploration of unknown aspects of yourself").
symbol(house, _, "Representation of self, security, or different aspects of personality").
symbol(car, driving, "Control over your life path or direction").
symbol(car, passenger, "Feeling that others are controlling your journey").
symbol(car, broken, "Obstacles in your path or feeling stuck").
symbol(car, _, "Direction in life, personal journey, or control").
symbol(door, open, "New opportunities or pathways available to you").
symbol(door, locked, "Blocked opportunities or resistance to change").
symbol(door, _, "New opportunities, transitions, or choices").
symbol(key, _, "Access, solutions, or hidden knowledge").
symbol(phone, _, "Communication issues or desire to connect").

/* Actions */
symbol(falling, _, "Feeling insecure, out of control, or letting go").
symbol(flying, _, "Freedom, breaking limitations, or gaining perspective").
symbol(running, chased, "Avoiding problems or feeling threatened").
symbol(running, exercise, "Progress, determination, or personal growth").
symbol(running, _, "Avoiding problems, fear, or ambition").
symbol(searching, _, "Seeking answers, purpose, or identity").

/* People */
symbol(stranger, _, "Unknown aspects of yourself or unfamiliar situations").
symbol(child, _, "Innocence, new beginnings, vulnerability").
symbol(ex_partner, _, "Unresolved feelings, lessons learned, or past patterns").
symbol(deceased, _, "Unresolved grief, final communications, or memory processing").

/* Settings */
symbol(school, _, "Learning, social anxiety, or past experiences").
symbol(work, _, "Ambitions, stress, or productivity concerns").
symbol(forest, _, "Unconscious mind, mystery, or feeling lost").
symbol(ocean, _, "Emotions, unconscious mind, or overwhelming feelings").

/* Conditions */
symbol(darkness, _, "Unknown, fear, or hidden aspects").
symbol(light, _, "Awareness, clarity, or enlightenment").
symbol(naked, _, "Vulnerability, exposure, or authenticity").
symbol(lost, _, "Uncertainty in life, seeking direction, or identity issues").

/* Rules for determining relevance of symbols */
is_relevant(Symbol, Description) :-
    sub_string(Description, _, _, _, Symbol).

/* Rule to find interpretation with context */
interpret(Symbol, Context, Interpretation) :-
    symbol(Symbol, Context, Interpretation), !.

/* Fallback rule for interpretation without specific context */
interpret(Symbol, _, Interpretation) :-
    symbol(Symbol, _, Interpretation).

/* Rule to generate overall interpretation from multiple symbols */
overall_interpretation([Symbol], Interpretation) :-
    interpret(Symbol, _, SymbolInterpretation),
    string_concat("Your dream about ", Symbol, Part1),
    string_concat(Part1, " suggests ", Part2),
    string_concat(Part2, SymbolInterpretation, Interpretation).

overall_interpretation(Symbols, Interpretation) :-
    Symbols = [_,_|_],  % At least two symbols
    string_concat("Your dream contains several symbols that together suggest ", Interpretation, _).