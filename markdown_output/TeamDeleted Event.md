       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TeamDeleted Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3340.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : TeamDeleted Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a team is successfully deleted. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event TeamDeleted As [TeamChangedEventHandler](topic5935.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim handler As [TeamChangedEventHandler](topic5935.md)
     
    AddHandler instance.TeamDeleted, handler  
  
C#|   
---|---  
      
    
    public event [TeamChangedEventHandler](topic5935.md) TeamDeleted  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)

©2024 DriveWorks Ltd. All Rights Reserved.
