ValidateFormula Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectUtility Class](topic4899.md) : ValidateFormula Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_formula_
    The formula to validate

Glossary Item Box

Determines if the given formula is valid or not. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function ValidateFormula( _
       ByVal _formula_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectUtility](topic4899.md)
    Dim formula As String
    Dim value As Boolean
     
    value = instance.ValidateFormula(formula)  
  
C#|   
---|---  
      
    
    public bool ValidateFormula( 
       string _formula_
    )  
  
#### Parameters

 _formula_
    The formula to validate

#### Return Value

True if the formula is valid.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectUtility Class](topic4899.md)   
[ProjectUtility Members](topic4900.md)


