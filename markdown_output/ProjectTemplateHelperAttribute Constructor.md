Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectTemplateHelperAttribute Constructor   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [ProjectTemplateHelperAttribute Class](topic2144.md) : ProjectTemplateHelperAttribute Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the project template helper.

_projectTemplateHelperType_
    The CLR type of the project template helper.

_standalone_
    True if the template helper can be instantiated without a corresponding template, otherwise false.

Glossary Item Box

Initializes a new instance of the [ProjectTemplateHelperAttribute](topic2144.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _name_ As String, _
       ByVal _projectTemplateHelperType_ As Type, _
       ByVal _standalone_ As Boolean _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim name As String
    Dim projectTemplateHelperType As Type
    Dim standalone As Boolean
     
    Dim instance As New [ProjectTemplateHelperAttribute](topic2144.md)(name, projectTemplateHelperType, standalone)  
  
C#|   
---|---  
      
    
    public ProjectTemplateHelperAttribute( 
       string _name_ ,
       Type _projectTemplateHelperType_ ,
       bool _standalone_
    )  
  
#### Parameters

 _name_
    The name of the project template helper.
_projectTemplateHelperType_
    The CLR type of the project template helper.
_standalone_
    True if the template helper can be instantiated without a corresponding template, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTemplateHelperAttribute Class](topic2144.md)   
[ProjectTemplateHelperAttribute Members](topic2145.md)


