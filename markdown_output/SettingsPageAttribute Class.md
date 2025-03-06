![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SettingsPageAttribute Class   
[Members](topic960.md) See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic959.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : SettingsPageAttribute Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Exports a settings page from a library so that it can be shown in the settings window. 

# ![](dotnetimages/collapse.gif)Object Model

![](dotnetdiagramimages/image31.png)

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Assembly, 
       AllowMultiple=True, 
       Inherited=True)>
    Public Class SettingsPageAttribute 
       Inherits [DriveWorks.Extensibility.ExtensibilityAttribute](topic7177.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [SettingsPageAttribute](topic959.md)  
  
C#|   
---|---  
      
    
    [AttributeUsageAttribute(ValidOn=AttributeTargets.Assembly, 
       AllowMultiple=true, 
       Inherited=true)]
    public class SettingsPageAttribute : [DriveWorks.Extensibility.ExtensibilityAttribute](topic7177.md)   
  
# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
System.Attribute  
[DriveWorks.Extensibility.ExtensibilityAttribute](topic7177.md)  
**DriveWorks.Applications.SettingsPageAttribute**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SettingsPageAttribute Members](topic960.md)   
[DriveWorks.Applications Namespace](topic16.md)

©2024 DriveWorks Ltd. All Rights Reserved.
