![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
WindowsAuthentication Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5416.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SqlServerDataTable Class](topic5396.md) : WindowsAuthentication Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Whether to use Windows authentication to sign into the SQL database. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property WindowsAuthentication As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [SqlServerDataTable](topic5396.md)
    Dim value As Boolean
     
    instance.WindowsAuthentication = value
     
    value = instance.WindowsAuthentication  
  
C#|   
---|---  
      
    
    public bool WindowsAuthentication {get; set;}  
  
# ![](dotnetimages/collapse.gif)Remarks

Setting this value to true will clear the currently stored Username and Password.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SqlServerDataTable Class](topic5396.md)   
[SqlServerDataTable Members](topic5397.md)

©2024 DriveWorks Ltd. All Rights Reserved.
