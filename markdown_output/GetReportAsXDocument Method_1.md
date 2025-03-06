![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetReportAsXDocument Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReports Class](topic3272.md) : GetReportAsXDocument Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_reportId_
    The unique identifier of the report to get.

Glossary Item Box

Gets a report as XML stored in an XDocument. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetReportAsXDocument( _
       ByVal _reportId_ As Guid _
    ) As XDocument  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupReports](topic3272.md)
    Dim reportId As Guid
    Dim value As XDocument
     
    value = instance.GetReportAsXDocument(reportId)  
  
C#|   
---|---  
      
    
    public XDocument GetReportAsXDocument( 
       Guid _reportId_
    )  
  
#### Parameters

 _reportId_
    The unique identifier of the report to get.

#### Return Value

An instance of the System.Xml.Linq.XDocument class.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupReports Class](topic3272.md)   
[GroupReports Members](topic3273.md)


