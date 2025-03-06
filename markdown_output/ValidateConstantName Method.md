       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ValidateConstantName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [ValidationUtility Class](topic13287.md) : ValidateConstantName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_constant_
    

Glossary Item Box

Validates a DriveWorks Constant name 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ValidateConstantName( _
       ByVal _constant_ As String _
    ) As [ValidateNameResult](topic13193.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim constant As String
    Dim value As [ValidateNameResult](topic13193.md)
     
    value = [ValidationUtility](topic13287.md).ValidateConstantName(constant)  
  
C#|   
---|---  
      
    
    public static [ValidateNameResult](topic13193.md) ValidateConstantName( 
       string _constant_
    )  
  
#### Parameters

 _constant_
    

#### Return Value

True if value contains bad characters.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ValidationUtility Class](topic13287.md)   
[ValidationUtility Members](topic13288.md)


