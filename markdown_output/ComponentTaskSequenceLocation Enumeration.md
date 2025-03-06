![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ComponentTaskSequenceLocation Enumeration   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) : ComponentTaskSequenceLocation Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Represents the different locations in the generation sequence that tasks can scheduled for execution. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <FlagsAttribute()>
    Public Enum ComponentTaskSequenceLocation 
       Inherits System.Enum  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskSequenceLocation](topic6406.md)  
  
C#|   
---|---  
      
    
    [FlagsAttribute()]
    public enum ComponentTaskSequenceLocation : System.Enum   
  
# ![](dotnetimages/collapse.gif)Members

Member| Description  
---|---  
**After**|  Indicates that the task can run after the core generation sequence.  
**All**|  Indicates that the task can run in all task sequence locations.  
**Before**|  Indicates that the task can run before the core generation sequence.  
**None**|  Default value, indicates this task cannot run in any location.  
**PostClose**|  Indicates that the task can run after the model has been closed.  
**PostCopy**|  Indicates that the task can run after the model has been copied.  
**PreClose**|  Indicates that the task can run before the model has been closed.  
**PreCopy**|  Indicates that the task can run before the model has been copied.  
  
# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Components.Tasks.ComponentTaskSequenceLocation**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DriveWorks.Components.Tasks Namespace](topic6391.md)


