![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DocumentDesignerAttribute Class   
[Members](topic1569.md) See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1568.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.Documents Namespace](topic1507.md) : DocumentDesignerAttribute Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Applied to a class implementing the [IDocumentDesigner](topic1517.md) interface to provide information about the document designer. 

# ![](dotnetimages/collapse.gif)Object Model

![](dotnetdiagramimages/image56.png)

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=False, 
       Inherited=True)>
    Public Class DocumentDesignerAttribute 
       Inherits System.Attribute  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [DocumentDesignerAttribute](topic1568.md)  
  
C#|   
---|---  
      
    
    [AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=false, 
       Inherited=true)]
    public class DocumentDesignerAttribute : System.Attribute   
  
# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
System.Attribute  
**DriveWorks.Applications.Administrator.Extensibility.Documents.DocumentDesignerAttribute**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DocumentDesignerAttribute Members](topic1569.md)   
[DriveWorks.Applications.Administrator.Extensibility.Documents Namespace](topic1507.md)

©2024 DriveWorks Ltd. All Rights Reserved.
