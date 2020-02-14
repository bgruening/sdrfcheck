package uk.ac.ebi.fg.annotare2.magetabcheck.checks.idf;

import uk.ac.ebi.fg.annotare2.magetabcheck.checker.annotation.MageTabCheck;
import uk.ac.ebi.fg.annotare2.magetabcheck.checks.NonEmptyRangeCheck;
import uk.ac.ebi.fg.annotare2.magetabcheck.model.idf.ExperimentalFactor;

/**
 * @author Olga Melnichuk
 */
@MageTabCheck(
        ref = "EF01",
        value = "An experiment must have at least one experimental variable specified")
public class ListOfExperimentalFactorsMustBeNonEmpty extends NonEmptyRangeCheck<ExperimentalFactor> {
    public ListOfExperimentalFactorsMustBeNonEmpty() {
        super(factor -> factor != null &&
                factor.getType() != null &&
                factor.getType().getName() != null &&
                factor.getType().getName().getValue() != null &&
                factor.getName() != null &&
                factor.getName().getValue() != null);
    }
}