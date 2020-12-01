# Include all types of entities/categories in training data, not just the new ones
    # => avoids "forgetting"
# Label scheme should be consistent and not too specific ("CLOTHING" not "ADULT_CLOTHING")
    # => otherwise the model might not learn properly
    # going from generic to specific through a rule based system later on is possible