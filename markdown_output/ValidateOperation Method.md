ValidateOperation Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [ValidationUtility Class](topic13287.md) : ValidateOperation Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_operation_
    The name to validate.

Glossary Item Box

Validates a DriveWorks operation name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ValidateOperation( _
       ByVal _operation_ As String _
    ) As [ValidateNameResult](topic13193.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim operation As String
    Dim value As [ValidateNameResult](topic13193.md)
     
    value = [ValidationUtility](topic13287.md).ValidateOperation(operation)  
  
C#|   
---|---  
      
    
    public static [ValidateNameResult](topic13193.md) ValidateOperation( 
       string _operation_
    )  
  
#### Parameters

 _operation_
    The name to validate.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ValidationUtility Class](topic13287.md)   
[ValidationUtility Members](topic13288.md)


