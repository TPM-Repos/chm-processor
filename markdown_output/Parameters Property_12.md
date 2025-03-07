Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Parameters Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [IComponentTask Interface](topic6393.md) : Parameters Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all capturable parameters for the task. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property Parameters As [ComponentTaskParameterInfo()](topic6603.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IComponentTask](topic6393.md)
    Dim value() As [ComponentTaskParameterInfo](topic6603.md)
     
    value = instance.Parameters  
  
C#|   
---|---  
      
    
    [ComponentTaskParameterInfo[]](topic6603.md) Parameters {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IComponentTask Interface](topic6393.md)   
[IComponentTask Members](topic6394.md)


