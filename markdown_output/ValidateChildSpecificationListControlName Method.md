ValidateChildSpecificationListControlName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [ValidationUtility Class](topic13287.md) : ValidateChildSpecificationListControlName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    

Glossary Item Box

Validates a DriveWorks control name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ValidateChildSpecificationListControlName( _
       ByVal _name_ As String _
    ) As [ValidateNameResult](topic13193.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim name As String
    Dim value As [ValidateNameResult](topic13193.md)
     
    value = [ValidationUtility](topic13287.md).ValidateChildSpecificationListControlName(name)  
  
C#|   
---|---  
      
    
    public static [ValidateNameResult](topic13193.md) ValidateChildSpecificationListControlName( 
       string _name_
    )  
  
#### Parameters

 _name_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ValidationUtility Class](topic13287.md)   
[ValidationUtility Members](topic13288.md)


