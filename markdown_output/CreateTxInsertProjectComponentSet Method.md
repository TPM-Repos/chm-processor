![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxInsertProjectComponentSet Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxInsertProjectComponentSet Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name to give the component. This may be null to have one generated from captured component's name.

_capturedComponentId_
    The unique identifier of the captured component that you wish to add to the current project.

_index_
    

Glossary Item Box

Creates a transaction that will insert a component at the specified position in the current collection in the current project. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxInsertProjectComponentSet( _
       ByVal _name_ As String, _
       ByVal _capturedComponentId_ As Guid, _
       ByVal _index_ As Integer _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim name As String
    Dim capturedComponentId As Guid
    Dim index As Integer
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxInsertProjectComponentSet(name, capturedComponentId, index)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxInsertProjectComponentSet( 
       string _name_ ,
       Guid _capturedComponentId_ ,
       int _index_
    )  
  
#### Parameters

 _name_
    The name to give the component. This may be null to have one generated from captured component's name.
_capturedComponentId_
    The unique identifier of the captured component that you wish to add to the current project.
_index_
    

#### Return Value

A transaction that will perform the operation.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


