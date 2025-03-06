![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetRootNodeData Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [JsonDocument Class](topic3635.md) : GetRootNodeData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_reload_
    A flag which indicates whether the nodes should be reloaded from the documents last committed state.

Glossary Item Box

Gets the documents tree structure. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetRootNodeData( _
       Optional ByVal _reload_ As Boolean _
    ) As IEnumerable(Of JsonDocumentNodeData)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [JsonDocument](topic3635.md)
    Dim reload As Boolean
    Dim value As IEnumerable(Of JsonDocumentNodeData)
     
    value = instance.GetRootNodeData(reload)  
  
C#|   
---|---  
      
    
    public IEnumerable<JsonDocumentNodeData> GetRootNodeData( 
       bool _reload_
    )  
  
#### Parameters

 _reload_
    A flag which indicates whether the nodes should be reloaded from the documents last committed state.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[JsonDocument Class](topic3635.md)   
[JsonDocument Members](topic3636.md)


