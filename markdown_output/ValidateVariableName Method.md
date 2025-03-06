ValidateVariableName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [ValidationUtility Class](topic13287.md) : ValidateVariableName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_variable_
    

Glossary Item Box

Validates a DriveWorks Variable Name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ValidateVariableName( _
       ByVal _variable_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim variable As String
    Dim value As Boolean
     
    value = [ValidationUtility](topic13287.md).ValidateVariableName(variable)  
  
C#|   
---|---  
      
    
    public static bool ValidateVariableName( 
       string _variable_
    )  
  
#### Parameters

 _variable_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ValidationUtility Class](topic13287.md)   
[ValidationUtility Members](topic13288.md)


