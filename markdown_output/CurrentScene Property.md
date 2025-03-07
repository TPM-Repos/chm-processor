Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CurrentScene Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [PreviewControl Class](topic8709.md) : CurrentScene Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a Json string version of the current scene. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Property CurrentScene As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [PreviewControl](topic8709.md)
    Dim value As String
     
    instance.CurrentScene = value
     
    value = instance.CurrentScene  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public string CurrentScene {get; set;}  
  
#### Property Value

A Json string version of the current scene.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[PreviewControl Class](topic8709.md)   
[PreviewControl Members](topic8710.md)


