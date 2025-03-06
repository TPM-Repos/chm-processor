![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateNameSearchProcess Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectUtility Class](topic4899.md) : CreateNameSearchProcess Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_referenceName_
    The name to search for.

Glossary Item Box

Creates a new process capable of searching for named items in all rules in the project. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateNameSearchProcess( _
       ByVal _referenceName_ As String _
    ) As [NameSearchProcess](topic13195.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectUtility](topic4899.md)
    Dim referenceName As String
    Dim value As [NameSearchProcess](topic13195.md)
     
    value = instance.CreateNameSearchProcess(referenceName)  
  
C#|   
---|---  
      
    
    public [NameSearchProcess](topic13195.md) CreateNameSearchProcess( 
       string _referenceName_
    )  
  
#### Parameters

 _referenceName_
    The name to search for.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectUtility Class](topic4899.md)   
[ProjectUtility Members](topic4900.md)


