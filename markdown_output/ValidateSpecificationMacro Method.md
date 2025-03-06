ValidateSpecificationMacro Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [ValidationUtility Class](topic13287.md) : ValidateSpecificationMacro Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_macro_
    The name to validate.

Glossary Item Box

Validates a DriveWorks specification macro name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ValidateSpecificationMacro( _
       ByVal _macro_ As String _
    ) As [ValidateNameResult](topic13193.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim macro As String
    Dim value As [ValidateNameResult](topic13193.md)
     
    value = [ValidationUtility](topic13287.md).ValidateSpecificationMacro(macro)  
  
C#|   
---|---  
      
    
    public static [ValidateNameResult](topic13193.md) ValidateSpecificationMacro( 
       string _macro_
    )  
  
#### Parameters

 _macro_
    The name to validate.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ValidationUtility Class](topic13287.md)   
[ValidationUtility Members](topic13288.md)


