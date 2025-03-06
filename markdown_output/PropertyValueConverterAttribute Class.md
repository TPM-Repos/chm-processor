![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PropertyValueConverterAttribute Class   
[Members](topic9482.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) : PropertyValueConverterAttribute Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Marks a CLR type with a corresponding property value converter. 

# ![](dotnetimages/collapse.gif)Object Model

![](dotnetdiagramimages/image451.png)

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Class Or  _
        AttributeTargets.Struct Or  _
        AttributeTargets.Interface, 
       AllowMultiple=False, 
       Inherited=True)>
    Public NotInheritable Class PropertyValueConverterAttribute 
       Inherits System.Attribute  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [PropertyValueConverterAttribute](topic9481.md)  
  
C#|   
---|---  
      
    
    [AttributeUsageAttribute(ValidOn=AttributeTargets.Class | 
        AttributeTargets.Struct | 
        AttributeTargets.Interface, 
       AllowMultiple=false, 
       Inherited=true)]
    public sealed class PropertyValueConverterAttribute : System.Attribute   
  
# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
System.Attribute  
**DriveWorks.Forms.DataModel.PropertyValueConverterAttribute**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[PropertyValueConverterAttribute Members](topic9482.md)   
[DriveWorks.Forms.DataModel Namespace](topic9371.md)


