![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FileFormatGenerateTaskAttribute Class   
[Members](topic13572.md)   
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) : FileFormatGenerateTaskAttribute Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Attribute that should be assigned to tasks that inherits from the file format generator base task. 

# ![](dotnetimages/collapse.gif)Object Model

![](dotnetdiagramimages/image736.png)

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=True, 
       Inherited=True)>
    Public NotInheritable Class FileFormatGenerateTaskAttribute 
       Inherits [FileExtensionAttribute](topic13564.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [FileFormatGenerateTaskAttribute](topic13571.md)  
  
C#|   
---|---  
      
    
    [AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=true, 
       Inherited=true)]
    public sealed class FileFormatGenerateTaskAttribute : [FileExtensionAttribute](topic13564.md)   
  
# ![](dotnetimages/collapse.gif)Remarks

This can be applied multiple times for the same class if that class converts more than one file extension.

# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
System.Attribute  
[DriveWorks.SolidWorks.FileExtensionAttribute](topic13564.md)  
**DriveWorks.SolidWorks.FileFormatGenerateTaskAttribute**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[FileFormatGenerateTaskAttribute Members](topic13572.md)   
[DriveWorks.SolidWorks Namespace](topic13345.md)


