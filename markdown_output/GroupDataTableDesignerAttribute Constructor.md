![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GroupDataTableDesignerAttribute Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1494.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.DataTables Namespace](topic1432.md) > [GroupDataTableDesignerAttribute Class](topic1488.md) : GroupDataTableDesignerAttribute Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_groupDataTableType_
    The type of group data table supported by the designer (must be derived from [DriveWorks.GroupDataTable](topic3110.md)).

_displayName_
    The localizable display name of the group data table type.

_image_
    The localizable image of the group data table type.

Glossary Item Box

Initializes a new instance of the [GroupDataTableDesignerAttribute](topic1488.md) attribute class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _groupDataTableType_ As Type, _
       ByVal _displayName_ As String, _
       ByVal _image_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim groupDataTableType As Type
    Dim displayName As String
    Dim image As String
     
    Dim instance As New [GroupDataTableDesignerAttribute](topic1488.md)(groupDataTableType, displayName, image)  
  
C#|   
---|---  
      
    
    public GroupDataTableDesignerAttribute( 
       Type _groupDataTableType_ ,
       string _displayName_ ,
       string _image_
    )  
  
#### Parameters

 _groupDataTableType_
    The type of group data table supported by the designer (must be derived from [DriveWorks.GroupDataTable](topic3110.md)).
_displayName_
    The localizable display name of the group data table type.
_image_
    The localizable image of the group data table type.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupDataTableDesignerAttribute Class](topic1488.md)   
[GroupDataTableDesignerAttribute Members](topic1489.md)

©2024 DriveWorks Ltd. All Rights Reserved.
