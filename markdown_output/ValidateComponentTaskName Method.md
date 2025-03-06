       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ValidateComponentTaskName Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13301.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [ValidationUtility Class](topic13287.md) : ValidateComponentTaskName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_taskName_
    The name to validate.

Glossary Item Box

Validates a DriveWorks component task name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ValidateComponentTaskName( _
       ByVal _taskName_ As String _
    ) As [ValidateNameResult](topic13193.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim taskName As String
    Dim value As [ValidateNameResult](topic13193.md)
     
    value = [ValidationUtility](topic13287.md).ValidateComponentTaskName(taskName)  
  
C#|   
---|---  
      
    
    public static [ValidateNameResult](topic13193.md) ValidateComponentTaskName( 
       string _taskName_
    )  
  
#### Parameters

 _taskName_
    The name to validate.

#### Return Value

The result of the validation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ValidationUtility Class](topic13287.md)   
[ValidationUtility Members](topic13288.md)

©2024 DriveWorks Ltd. All Rights Reserved.
