       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ValidateFormula Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4926.md)  
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

©2024 DriveWorks Ltd. All Rights Reserved.
