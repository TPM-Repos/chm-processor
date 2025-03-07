Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsRuleProfilingEnabled Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : IsRuleProfilingEnabled Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets whether projects loaded in this specification group should have profiling enabled. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property IsRuleProfilingEnabled As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim value As Boolean
     
    instance.IsRuleProfilingEnabled = value
     
    value = instance.IsRuleProfilingEnabled  
  
C#|   
---|---  
      
    
    public bool IsRuleProfilingEnabled {get; set;}  
  
# Remarks

A specification group is the entire family for a specification (all related specifications e.g. parent, children and siblings etc).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


