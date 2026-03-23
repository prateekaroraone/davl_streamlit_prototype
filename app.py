import streamlit as st
from validate import validate_decision, load_registry
from score import compute_score
from action_engine import take_action

st.title("Decision-Aware Validation Layer Prototype")

# Load decision registry
registry = load_registry()
decision_names = [d['name'] for d in registry]
selected_decision = st.selectbox("Select a decision to validate", decision_names)

decision = next(d for d in registry if d['name'] == selected_decision)

# Validate
validation_results = validate_decision(decision)
st.subheader("Validation Results")
st.json(validation_results)

# Score
scores = compute_score(validation_results)
st.subheader("Decision Scores")
st.json(scores)

# Suggested actions
st.subheader("Recommended Actions")
take_action(selected_decision, scores)
