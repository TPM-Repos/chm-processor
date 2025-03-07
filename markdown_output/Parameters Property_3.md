Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Parameters Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [GenerationTask Class](topic13678.md) : Parameters Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

When overridden, provides a collection of capturable parameters for this task. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overridable ReadOnly Property Parameters As [ComponentTaskParameterInfo()](topic6603.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GenerationTask](topic13678.md)
    Dim value() As [ComponentTaskParameterInfo](topic6603.md)
     
    value = instance.Parameters  
  
C#|   
---|---  
      
    
    public virtual [ComponentTaskParameterInfo[]](topic6603.md) Parameters {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GenerationTask Class](topic13678.md)   
[GenerationTask Members](topic13679.md)


