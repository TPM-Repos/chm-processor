![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConfigurationReportItem Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [ConfigurationReportItem Class](topic9677.md) : ConfigurationReportItem Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_displayName_
    The name of the item.

_isMissing_
    True if the item is missing from the source group or machine, otherwise False.

Glossary Item Box

Creates a new instance of [ConfigurationReportItem](topic9677.md). 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _displayName_ As String, _
       ByVal _isMissing_ As Boolean _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim displayName As String
    Dim isMissing As Boolean
     
    Dim instance As New [ConfigurationReportItem](topic9677.md)(displayName, isMissing)  
  
C#|   
---|---  
      
    
    public ConfigurationReportItem( 
       string _displayName_ ,
       bool _isMissing_
    )  
  
#### Parameters

 _displayName_
    The name of the item.
_isMissing_
    True if the item is missing from the source group or machine, otherwise False.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ConfigurationReportItem Class](topic9677.md)   
[ConfigurationReportItem Members](topic9678.md)


