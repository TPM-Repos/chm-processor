Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FileFormatGeneratorAttribute Class   
[Members](topic13608.md)   
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) : FileFormatGeneratorAttribute Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Attribute that should be assigned to inheritors of [FileFormatGenerator](topic13579.md) to specify their target file extensions. 

# Object Model

![](dotnetdiagramimages/image738.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=True, 
       Inherited=True)>
    Public NotInheritable Class FileFormatGeneratorAttribute 
       Inherits [FileExtensionAttribute](topic13564.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FileFormatGeneratorAttribute](topic13607.md)  
  
C#|   
---|---  
      
    
    [AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=true, 
       Inherited=true)]
    public sealed class FileFormatGeneratorAttribute : [FileExtensionAttribute](topic13564.md)   
  
# Remarks

This can be applied multiple times for the same class if that class converts more than one file extension.

# Inheritance Hierarchy

System.Object  
System.Attribute  
[DriveWorks.SolidWorks.FileExtensionAttribute](topic13564.md)  
**DriveWorks.SolidWorks.FileFormatGeneratorAttribute**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FileFormatGeneratorAttribute Members](topic13608.md)   
[DriveWorks.SolidWorks Namespace](topic13345.md)


