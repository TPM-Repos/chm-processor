![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SqlDataSourceConfiguration Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6813.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Connectors.Database Namespace](topic6754.md) > [SqlDataSourceConfiguration Class](topic6807.md) : SqlDataSourceConfiguration Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_data_
    The XML to use for this configuration.

Glossary Item Box

Creates a new instance of the [SqlDataSourceConfiguration](topic6807.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _data_ As XElement _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim data As XElement
     
    Dim instance As New [SqlDataSourceConfiguration](topic6807.md)(data)  
  
C#|   
---|---  
      
    
    public SqlDataSourceConfiguration( 
       XElement _data_
    )  
  
#### Parameters

 _data_
    The XML to use for this configuration.

# ![](dotnetimages/collapse.gif)Remarks

The XML will be live edited as properties change in this configuration.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SqlDataSourceConfiguration Class](topic6807.md)   
[SqlDataSourceConfiguration Members](topic6808.md)

©2024 DriveWorks Ltd. All Rights Reserved.
