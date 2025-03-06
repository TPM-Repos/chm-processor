       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RootProfileEvents Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4725.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectProfiler Class](topic4712.md) : RootProfileEvents Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the root events that have been recorded while the profiler is enabled. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property RootProfileEvents As IReadOnlyList(Of ProjectProfileEventBase)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectProfiler](topic4712.md)
    Dim value As IReadOnlyList(Of ProjectProfileEventBase)
     
    value = instance.RootProfileEvents  
  
C#|   
---|---  
      
    
    public IReadOnlyList<ProjectProfileEventBase> RootProfileEvents {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectProfiler Class](topic4712.md)   
[ProjectProfiler Members](topic4713.md)

©2024 DriveWorks Ltd. All Rights Reserved.
