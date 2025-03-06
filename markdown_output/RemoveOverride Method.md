       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RemoveOverride Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic194.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandOverrideService Interface](topic188.md) : RemoveOverride Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_commandOverride_
    The command override to remove.

Glossary Item Box

Removes the specified command override. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function RemoveOverride( _
       ByVal _commandOverride_ As [ICommandOverride](topic180.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommandOverrideService](topic188.md)
    Dim commandOverride As [ICommandOverride](topic180.md)
    Dim value As Boolean
     
    value = instance.RemoveOverride(commandOverride)  
  
C#|   
---|---  
      
    
    bool RemoveOverride( 
       [ICommandOverride](topic180.md) _commandOverride_
    )  
  
#### Parameters

 _commandOverride_
    The command override to remove.

#### Return Value

True if the override was removed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommandOverrideService Interface](topic188.md)   
[ICommandOverrideService Members](topic189.md)

©2024 DriveWorks Ltd. All Rights Reserved.
