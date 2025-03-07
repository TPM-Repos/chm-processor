Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EstimatedResultCount Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IGroupResultEnumerator Interface](topic2213.md) : EstimatedResultCount Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a count of the results expected to be retrieved by the enumerator. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property EstimatedResultCount As Integer  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IGroupResultEnumerator](topic2213.md)
    Dim value As Integer
     
    value = instance.EstimatedResultCount  
  
C#|   
---|---  
      
    
    int EstimatedResultCount {get;}  
  
#### Property Value

The estimated result count, or -1 if not supported.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IGroupResultEnumerator Interface](topic2213.md)   
[IGroupResultEnumerator Members](topic2214.md)


