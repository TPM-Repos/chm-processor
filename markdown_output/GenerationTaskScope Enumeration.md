![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GenerationTaskScope Enumeration   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) : GenerationTaskScope Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Specifies the type of SOLIDWORKS components a [GenerationTask](topic13678.md) support. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <FlagsAttribute()>
    Public Enum GenerationTaskScope 
       Inherits System.Enum  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GenerationTaskScope](topic13452.md)  
  
C#|   
---|---  
      
    
    [FlagsAttribute()]
    public enum GenerationTaskScope : System.Enum   
  
# ![](dotnetimages/collapse.gif)Members

Member| Description  
---|---  
**All**|  Specifies that the [GenerationTask](topic13678.md) supports running on all types of components.  
**Assemblies**|  Specifies that the [GenerationTask](topic13678.md) supports running on assemblies.  
**Drawings**|  Specifies that the [GenerationTask](topic13678.md) supports running on drawings.  
**Parts**|  Specifies that the [GenerationTask](topic13678.md) supports running on parts.  
  
# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.SolidWorks.GenerationTaskScope**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DriveWorks.SolidWorks Namespace](topic13345.md)


