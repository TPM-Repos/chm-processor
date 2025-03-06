![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ApplicationPluginAttribute Class   
[Members](topic2107.md) See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2106.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) : ApplicationPluginAttribute Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides information about an application plugin to a DriveWorks Application. 

# ![](dotnetimages/collapse.gif)Object Model

![](dotnetdiagramimages/image72.png)

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=False, 
       Inherited=False)>
    Public NotInheritable Class ApplicationPluginAttribute 
       Inherits System.Attribute  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ApplicationPluginAttribute](topic2106.md)  
  
C#|   
---|---  
      
    
    [AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=false, 
       Inherited=false)]
    public sealed class ApplicationPluginAttribute : System.Attribute   
  
# ![](dotnetimages/collapse.gif)Remarks

A class which implements the [IApplicationPlugin](topic2004.md) interface must also be marked with this attribute to be recognized as an application plugin.

# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
System.Attribute  
**DriveWorks.Applications.Extensibility.ApplicationPluginAttribute**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ApplicationPluginAttribute Members](topic2107.md)   
[DriveWorks.Applications.Extensibility Namespace](topic1995.md)

©2024 DriveWorks Ltd. All Rights Reserved.
