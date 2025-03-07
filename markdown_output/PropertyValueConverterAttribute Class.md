Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
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

# Object Model

![](dotnetdiagramimages/image451.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Class Or  _
        AttributeTargets.Struct Or  _
        AttributeTargets.Interface, 
       AllowMultiple=False, 
       Inherited=True)>
    Public NotInheritable Class PropertyValueConverterAttribute 
       Inherits System.Attribute  
  
Visual Basic (Usage)| Copy Code  
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
  
# Inheritance Hierarchy

System.Object  
System.Attribute  
**DriveWorks.Forms.DataModel.PropertyValueConverterAttribute**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[PropertyValueConverterAttribute Members](topic9482.md)   
[DriveWorks.Forms.DataModel Namespace](topic9371.md)


