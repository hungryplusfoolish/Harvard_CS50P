import pytest
import spectra

def test_BMI():
    with pytest.raises(TypeError):
          assert spectra.BMI("Cat")
    with pytest.raises(TypeError):
          assert spectra.BMI("Dog")
    assert spectra.BMI(172.72,89.3424036281179) == "You're Body Mass Index is: 29.95."
    assert spectra.BMI(162.56,58.95691609977324) == "You're Body Mass Index is: 22.31."

def test_BFP():
      with pytest.raises(TypeError):
            assert spectra.BFP("Cat")
      with pytest.raises(TypeError):
            assert spectra.BFP("Dog")
      assert spectra.BFP(182.88,38.608,102.108,'M') == "Your Body Fat Percentage is: 27%."
      assert spectra.BFP(165.1,35.56,40.6,'F',127.0) == "Your Body Fat Percentage is: 24%."



def test_BMR():
      with pytest.raises(TypeError):
            assert spectra.BMR("Cat")
      with pytest.raises(TypeError):
            assert spectra.BMR("Dog")
      assert spectra.BMR(172.72,89.3424036281179,24,'M') == "You're Base Metabolic Rate is: 1,978/day."
      assert spectra.BMR(162.56,58.95691609977324,22,'F') == "You're Base Metabolic Rate is: 1,401/day."

      
