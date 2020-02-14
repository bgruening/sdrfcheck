/*
 * Copyright 2012 EMBL - European Bioinformatics Institute
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package uk.ac.ebi.fg.annotare2.magetabcheck.checks.idf;

import uk.ac.ebi.fg.annotare2.magetabcheck.checker.annotation.MageTabCheck;
import uk.ac.ebi.fg.annotare2.magetabcheck.checks.RangeCheck;
import uk.ac.ebi.fg.annotare2.magetabcheck.model.idf.Comment;

import static com.google.common.collect.Range.singleton;

/**
 * @author Olga Melnichuk
 */
@MageTabCheck(
        ref = "COM01",
        value = "Non-empty value for 'Comment[AEExperimentType]' must be provided in IDF")
public class AeExperimentTypeCommentRequired extends RangeCheck<Comment> {

    public AeExperimentTypeCommentRequired() {
        super(comment -> "AEExperimentType".equals(comment.getName()), singleton(1));
    }
}
