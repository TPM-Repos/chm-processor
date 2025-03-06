       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
WillExecute Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9653.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [AddGroupUserToTeamAction Class](topic9643.md) : WillExecute Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Returns whether or not this action wants to execute. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides ReadOnly Property WillExecute As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [AddGroupUserToTeamAction](topic9643.md)
    Dim value As Boolean
     
    value = instance.WillExecute  
  
C#|   
---|---  
      
    
    public override bool WillExecute {get;}  
  
#### Property Value

True if it this action wants to execute.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[AddGroupUserToTeamAction Class](topic9643.md)   
[AddGroupUserToTeamAction Members](topic9644.md)

©2024 DriveWorks Ltd. All Rights Reserved.
