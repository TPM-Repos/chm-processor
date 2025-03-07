Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FunctionProfiles Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectProfiler Class](topic4712.md) : FunctionProfiles Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a collection of all seen function profiles that have been recorded while the profiler is enabled. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property FunctionProfiles As IReadOnlyList(Of ProjectFunctionProfile)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectProfiler](topic4712.md)
    Dim value As IReadOnlyList(Of ProjectFunctionProfile)
     
    value = instance.FunctionProfiles  
  
C#|   
---|---  
      
    
    public IReadOnlyList<ProjectFunctionProfile> FunctionProfiles {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectProfiler Class](topic4712.md)   
[ProjectProfiler Members](topic4713.md)


