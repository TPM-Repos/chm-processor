       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StatesToTriggerOn Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5142.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleasedTriggeredAction Class](topic5123.md) : StatesToTriggerOn Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the states that this action should be triggered on. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property StatesToTriggerOn As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedTriggeredAction](topic5123.md)
    Dim value As String
     
    instance.StatesToTriggerOn = value
     
    value = instance.StatesToTriggerOn  
  
C#|   
---|---  
      
    
    public string StatesToTriggerOn {get; set;}  
  
# Remarks

These states dictate the state the specification must be in for this trigger to run. If the specification is not in any of the states delcared, then the trigger with not automatically run.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedTriggeredAction Class](topic5123.md)   
[ReleasedTriggeredAction Members](topic5124.md)

©2024 DriveWorks Ltd. All Rights Reserved.
