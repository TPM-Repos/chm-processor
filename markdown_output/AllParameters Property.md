Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AllParameters Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [GenerationTask Class](topic13678.md) : AllParameters Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all capturable parameters for the task. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property AllParameters As [ComponentTaskParameterInfo()](topic6603.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GenerationTask](topic13678.md)
    Dim value() As [ComponentTaskParameterInfo](topic6603.md)
     
    value = instance.AllParameters  
  
C#|   
---|---  
      
    
    public [ComponentTaskParameterInfo[]](topic6603.md) AllParameters {get;}  
  
# Remarks

This includes both **DefaultParameters** and [Parameters](topic13690.md).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GenerationTask Class](topic13678.md)   
[GenerationTask Members](topic13679.md)


