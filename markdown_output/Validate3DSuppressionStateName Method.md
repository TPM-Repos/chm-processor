Validate3DSuppressionStateName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [ValidationUtility Class](topic13287.md) : Validate3DSuppressionStateName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name to validate

Glossary Item Box

Validates a 3D document's suppression state name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function Validate3DSuppressionStateName( _
       ByVal _name_ As String _
    ) As [ValidateNameResult](topic13193.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim name As String
    Dim value As [ValidateNameResult](topic13193.md)
     
    value = [ValidationUtility](topic13287.md).Validate3DSuppressionStateName(name)  
  
C#|   
---|---  
      
    
    public static [ValidateNameResult](topic13193.md) Validate3DSuppressionStateName( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name to validate

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ValidationUtility Class](topic13287.md)   
[ValidationUtility Members](topic13288.md)


