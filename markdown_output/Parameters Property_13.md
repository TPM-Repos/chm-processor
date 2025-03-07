Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Parameters Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [IComponentTaskCondition Interface](topic6399.md) : Parameters Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all capturable parameters for the [ComponentTaskReleaseCondition](topic6647.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property Parameters As [ComponentTaskParameterInfo()](topic6603.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IComponentTaskCondition](topic6399.md)
    Dim value() As [ComponentTaskParameterInfo](topic6603.md)
     
    value = instance.Parameters  
  
C#|   
---|---  
      
    
    [ComponentTaskParameterInfo[]](topic6603.md) Parameters {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IComponentTaskCondition Interface](topic6399.md)   
[IComponentTaskCondition Members](topic6400.md)


