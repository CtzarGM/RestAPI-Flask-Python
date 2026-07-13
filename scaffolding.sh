#!/bin/bash

# Define the root course directory
ROOT_DIR="inventory_engine_course"
mkdir -p "$ROOT_DIR"
cd "$ROOT_DIR" || exit

echo "🚀 Scaffolding Project-Driven Master Class Architecture..."

# Section 1
mkdir -p "sec01_intro_and_env/01_introduction_to_course" \
         "sec01_intro_and_env/02_meet_classmates_and_instructor" \
         "sec01_intro_and_env/03_environment_setup" \
         "sec01_intro_and_env/04_how_to_get_started" \
         "sec01_intro_and_env/05_installing_python_mac" \
         "sec01_intro_and_env/06_installing_python_windows"

# Section 2
mkdir -p "sec02_python_refresher/01_variables" \
         "sec02_python_refresher/02_string_formatting" \
         "sec02_python_refresher/03_getting_user_input" \
         "sec02_python_refresher/04_writing_first_python_app" \
         "sec02_python_refresher/05_lists_tuples_sets" \
         "sec02_python_refresher/06_lists_tuples_sets_deep_dive" \
         "sec02_python_refresher/07_booleans" \
         "sec02_python_refresher/08_advanced_sets_operations" \
         "sec02_python_refresher/09_if_statements" \
         "sec02_python_refresher/10_in_keyword" \
         "sec02_python_refresher/11_if_statements_with_in" \
         "sec02_python_refresher/12_loops_for" \
         "sec02_python_refresher/13_loops_while" \
         "sec02_python_refresher/14_flow_control_loops_ifs" \
         "sec02_python_refresher/15_list_comprehensions" \
         "sec02_python_refresher/16_dictionaries" \
         "sec02_python_refresher/17_dictionary_comprehensions" \
         "sec02_python_refresher/18_destructuring" \
         "sec02_python_refresher/19_dictionaries_called_students" \
         "sec02_python_refresher/20_functions" \
         "sec02_python_refresher/21_function_arguments" \
         "sec02_python_refresher/22_default_and_keyword_arguments" \
         "sec02_python_refresher/23_functions_returning_values" \
         "sec02_python_refresher/24_functions_deep_dive" \
         "sec02_python_refresher/25_lambda_functions" \
         "sec02_python_refresher/26_unpacking_args_kwargs" \
         "sec02_python_refresher/27_oop_in_python" \
         "sec02_python_refresher/28_magic_methods_str_repr" \
         "sec02_python_refresher/29_classes_and_objects" \
         "sec02_python_refresher/30_classmethod_and_staticmethod" \
         "sec02_python_refresher/31_classmethod_and_staticmethod_deep_dive" \
         "sec02_python_refresher/32_class_inheritance" \
         "sec02_python_refresher/33_class_composition" \
         "sec02_python_refresher/34_type_hinting" \
         "sec02_python_refresher/35_modules_and_imports" \
         "sec02_python_refresher/36_absolute_and_relative_imports" \
         "sec02_python_refresher/37_exceptions" \
         "sec02_python_refresher/38_custom_exception_classes" \
         "sec02_python_refresher/39_first_class_functions" \
         "sec02_python_refresher/40_simple_decorator" \
         "sec02_python_refresher/41_at_syntax_for_decorator" \
         "sec02_python_refresher/42_mutability_in_python" \
         "sec02_python_refresher/43_mutable_default_parameters" \
         "sec02_python_refresher/44_python_basics_quiz" \
         "sec02_python_refresher/45_keep_in_mind" \
         "sec02_python_refresher/46_map_function_explained" \
         "sec02_python_refresher/47_filter_function_explained"

# Section 3
mkdir -p "sec03_flask_basics/01_project_summary" \
         "sec03_flask_basics/02_initial_configuration" \
         "sec03_flask_basics/03_first_endpoint" \
         "sec03_flask_basics/04_what_is_json" \
         "sec03_flask_basics/05_testing_and_interacting" \
         "sec03_flask_basics/06_creating_shops" \
         "sec03_flask_basics/07_adding_products_to_shops" \
         "sec03_flask_basics/08_retrieving_specific_shop_and_products" \
         "sec03_flask_basics/09_flask_and_rest_api_basics_review"

# Section 4
mkdir -p "sec04_docker/01_containers_and_images" \
         "sec04_docker/02_download_resources" \
         "sec04_docker/03_running_flask_in_container" \
         "sec04_docker/04_virtualization_quiz"

# Section 5
mkdir -p "sec05_smorest_and_marshmallow/01_adding_dependencies_and_db" \
         "sec05_smorest_and_marshmallow/02_adding_new_endpoints" \
         "sec05_smorest_and_marshmallow/03_testing_endpoints_and_bugfixes" \
         "sec05_smorest_and_marshmallow/04_running_in_docker_with_autoreload" \
         "sec05_smorest_and_marshmallow/05_blueprints_and_methodviews_shops" \
         "sec05_smorest_and_marshmallow/06_blueprints_and_methodviews_products" \
         "sec05_smorest_and_marshmallow/07_marshmallow_schemas" \
         "sec05_smorest_and_marshmallow/08_data_validation" \
         "sec05_smorest_and_marshmallow/09_smorest_decorators" \
         "sec05_smorest_and_marshmallow/10_download_postman_collection" \
         "sec05_smorest_and_marshmallow/11_testing_after_marshmallow" \
         "sec05_smorest_and_marshmallow/12_smorest_and_marshmallow_review"

# Section 6
mkdir -p "sec06_sqlalchemy/01_pre_lecture_note" \
         "sec06_sqlalchemy/02_introduction_to_sqlalchemy" \
         "sec06_sqlalchemy/03_product_model_and_shop_model" \
         "sec06_sqlalchemy/04_one_to_many_relationships" \
         "sec06_sqlalchemy/05_flask_sqlalchemy_configuration" \
         "sec06_sqlalchemy/06_inserting_data_into_table" \
         "sec06_sqlalchemy/07_finding_models_by_id_or_404" \
         "sec06_sqlalchemy/08_updating_models" \
         "sec06_sqlalchemy/09_retrieving_all_models" \
         "sec06_sqlalchemy/10_deleting_models_with_cascading" \
         "sec06_sqlalchemy/11_testing_database_changes" \
         "sec06_sqlalchemy/12_sqlalchemy_basics_review"

# Section 7
mkdir -p "sec07_git/01_intro_to_git_and_commands" \
         "sec07_git/02_branches_and_branch_commands" \
         "sec07_git/03_remote_repositories_and_commands" \
         "sec07_git/04_advanced_git_commands" \
         "sec07_git/05_rebase_vs_merge_vs_squash" \
         "sec07_git/06_resolving_merge_conflicts" \
         "sec07_git/07_gitignore_necessity" \
         "sec07_git/08_git_submodules_and_tips" \
         "sec07_git/09_initializing_git_in_rest_api" \
         "sec07_git/10_test_git_knowledge"

# Section 8
mkdir -p "sec08_jwt/01_what_is_jwt" \
         "sec08_jwt/02_configuring_flask_jwt_extended" \
         "sec08_jwt/03_user_model_and_schema" \
         "sec08_jwt/04_registration_endpoint" \
         "sec08_jwt/05_login_endpoint" \
         "sec08_jwt/06_securing_endpoints_via_jwt" \
         "sec08_jwt/07_logout_feature" \
         "sec08_jwt/08_token_refreshing_overview" \
         "sec08_jwt/09_refreshing_tokens_implementation" \
         "sec08_jwt/10_testing_jwt_changes" \
         "sec08_jwt/11_jwt_basics_review"

# Section 9
mkdir -p "sec09_deployment/01_downloading_frontend_code" \
         "sec09_deployment/02_extracting_and_running_frontend" \
         "sec09_deployment/03_render_web_service_hosting" \
         "sec09_deployment/04_running_flask_gunicorn_docker" \
         "sec09_deployment/05_render_static_sites_frontend" \
         "sec09_deployment/06_test_finished_production_app" \
         "sec09_deployment/07_test_your_skills" \
         "sec09_deployment/08_conclusion_next_steps"

echo "✅ Folders successfully generated! Your complete workspace maps perfectly to the Master Class."