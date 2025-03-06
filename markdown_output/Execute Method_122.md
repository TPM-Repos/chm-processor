![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Execute Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [RemapSpecificationFolderAction Class](topic9970.md) : Execute Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_report_
    A method that can be used for reporting status.

Glossary Item Box

Executes this action. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides Function Execute( _
       ByVal _report_ As [ReportMethod](topic10006.md) _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [RemapSpecificationFolderAction](topic9970.md)
    Dim report As [ReportMethod](topic10006.md)
    Dim value As Boolean
     
    value = instance.Execute(report)  
  
C#|   
---|---  
      
    
    public override bool Execute( 
       [ReportMethod](topic10006.md) _report_
    )  
  
#### Parameters

 _report_
    A method that can be used for reporting status.

#### Return Value

False if there is a critical error that means the entire transfer process should end.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[RemapSpecificationFolderAction Class](topic9970.md)   
[RemapSpecificationFolderAction Members](topic9971.md)


