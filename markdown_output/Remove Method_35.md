       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Remove Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5706.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [TextDocumentLines Class](topic5691.md) : Remove Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_line_
    The line to remove.

Glossary Item Box

Removes the specified line from the document. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Remove( _
       ByVal _line_ As [TextDocumentLine](topic5659.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TextDocumentLines](topic5691.md)
    Dim line As [TextDocumentLine](topic5659.md)
     
    instance.Remove(line)  
  
C#|   
---|---  
      
    
    public void Remove( 
       [TextDocumentLine](topic5659.md) _line_
    )  
  
#### Parameters

 _line_
    The line to remove.

# Remarks

This will update the index of all lines afterwards.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TextDocumentLines Class](topic5691.md)   
[TextDocumentLines Members](topic5692.md)

©2024 DriveWorks Ltd. All Rights Reserved.
