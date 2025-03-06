![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectTemplateHelperAttribute Class   
[Members](topic2145.md) See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2144.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) : ProjectTemplateHelperAttribute Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Supports automatic discovery of project template helpers in a library. 

# ![](dotnetimages/collapse.gif)Object Model

![](dotnetdiagramimages/image76.png)

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Assembly, 
       AllowMultiple=True, 
       Inherited=True)>
    Public Class ProjectTemplateHelperAttribute 
       Inherits [DriveWorks.Extensibility.ExtensibilityAttribute](topic7177.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTemplateHelperAttribute](topic2144.md)  
  
C#|   
---|---  
      
    
    [AttributeUsageAttribute(ValidOn=AttributeTargets.Assembly, 
       AllowMultiple=true, 
       Inherited=true)]
    public class ProjectTemplateHelperAttribute : [DriveWorks.Extensibility.ExtensibilityAttribute](topic7177.md)   
  
# ![](dotnetimages/collapse.gif)Remarks

DriveWorks applications use this attribute to discover the project template helpers exposed by a library.

# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
System.Attribute  
[DriveWorks.Extensibility.ExtensibilityAttribute](topic7177.md)  
**DriveWorks.Applications.Extensibility.ProjectTemplateHelperAttribute**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTemplateHelperAttribute Members](topic2145.md)   
[DriveWorks.Applications.Extensibility Namespace](topic1995.md)

©2024 DriveWorks Ltd. All Rights Reserved.
