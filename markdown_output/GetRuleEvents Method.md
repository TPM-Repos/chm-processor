Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetRuleEvents Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectProfiler Class](topic4712.md) : GetRuleEvents Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all rule events in a flat chronological order. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetRuleEvents() As IEnumerable(Of ProjectRuleEvent)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectProfiler](topic4712.md)
    Dim value As IEnumerable(Of ProjectRuleEvent)
     
    value = instance.GetRuleEvents()  
  
C#|   
---|---  
      
    
    public IEnumerable<ProjectRuleEvent> GetRuleEvents()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectProfiler Class](topic4712.md)   
[ProjectProfiler Members](topic4713.md)


