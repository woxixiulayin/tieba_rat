                
Help on class _Element in module lxml.etree:

class _Element(__builtin__.object)
 |  Element class.
 |  
 |  References a document object and a libxml node.
 |  
 |  By pointing to a Document instance, a reference is kept to
 |  _Document as long as there is some pointer to a node in it.
 |  
 |  Methods defined here:
 |  
 |  __contains__(...)
 |      __contains__(self, element)
 |  
 |  __copy__(...)
 |      __copy__(self)
 |  
 |  __deepcopy__(...)
 |      __deepcopy__(self, memo)
 |  
 |  __delitem__(...)
 |      __delitem__(self, x)
 |      
 |      Deletes the given subelement or a slice.
 |  
 |  __getitem__(...)
 |      Returns the subelement at the given position or the requested
 |      slice.
 |  
 |  __iter__(...)
 |      __iter__(self)
 |  
 |  __len__(...)
 |      __len__(self)
 |      
 |      Returns the number of subelements.
 |  
 |  __nonzero__(...)
 |      x.__nonzero__() <==> x != 0
 |  
 |  __repr__(...)
 |      __repr__(self)
 |  
 |  __reversed__(...)
 |      __reversed__(self)
 |  
 |  __setitem__(...)
 |      __setitem__(self, x, value)
 |      
 |      Replaces the given subelement index or slice.
 |  
 |  addnext(...)
 |      addnext(self, element)
 |      
 |      Adds the element as a following sibling directly after this
 |      element.
 |      
 |      This is normally used to set a processing instruction or comment after
 |      the root node of a document.  Note that tail text is automatically
 |      discarded when adding at the root level.
 |  
 |  addprevious(...)
 |      addprevious(self, element)
 |      
 |      Adds the element as a preceding sibling directly before this
 |      element.
 |      
 |      This is normally used to set a processing instruction or comment
 |      before the root node of a document.  Note that tail text is
 |      automatically discarded when adding at the root level.
 |  
 |  append(...)
 |      append(self, element)
 |      
 |      Adds a subelement to the end of this element.
 |  
 |  clear(...)
 |      clear(self)
 |      
 |      Resets an element.  This function removes all subelements, clears
 |      all attributes and sets the text and tail properties to None.
 |  
 |  extend(...)
 |      extend(self, elements)
 |      
 |      Extends the current children by the elements in the iterable.
 |  
 |  find(...)
 |      find(self, path, namespaces=None)
 |      
 |      Finds the first matching subelement, by tag name or path.
 |      
 |      The optional ``namespaces`` argument accepts a
 |      prefix-to-namespace mapping that allows the usage of XPath
 |      prefixes in the path expression.
 |  
 |  findall(...)
 |      findall(self, path, namespaces=None)
 |      
 |      Finds all matching subelements, by tag name or path.
 |      
 |      The optional ``namespaces`` argument accepts a
 |      prefix-to-namespace mapping that allows the usage of XPath
 |      prefixes in the path expression.
 |  
 |  findtext(...)
 |      findtext(self, path, default=None, namespaces=None)
 |      
 |      Finds text for the first matching subelement, by tag name or path.
 |      
 |      The optional ``namespaces`` argument accepts a
 |      prefix-to-namespace mapping that allows the usage of XPath
 |      prefixes in the path expression.
 |  
 |  get(...)
 |      get(self, key, default=None)
 |      
 |      Gets an element attribute.
 |  
 |  getchildren(...)
 |      getchildren(self)
 |      
 |      Returns all direct children.  The elements are returned in document
 |      order.
 |      
 |      :deprecated: Note that this method has been deprecated as of
 |        ElementTree 1.3 and lxml 2.0.  New code should use
 |        ``list(element)`` or simply iterate over elements.
 |  
 |  getiterator(...)
 |      getiterator(self, tag=None)
 |      
 |      Returns a sequence or iterator of all elements in the subtree in
 |      document order (depth first pre-order), starting with this
 |      element.
 |      
 |      Can be restricted to find only elements with a specific tag
 |      (pass ``tag="xyz"``) or from a namespace (pass ``tag="{ns}*"``).
 |      
 |      You can also pass the Element, Comment, ProcessingInstruction and
 |      Entity factory functions to look only for the specific element type.
 |      
 |      :deprecated: Note that this method is deprecated as of
 |        ElementTree 1.3 and lxml 2.0.  It returns an iterator in
 |        lxml, which diverges from the original ElementTree
 |        behaviour.  If you want an efficient iterator, use the
 |        ``element.iter()`` method instead.  You should only use this
 |        method in new code if you require backwards compatibility
 |        with older versions of lxml or ElementTree.
 |  
 |  getnext(...)
 |      getnext(self)
 |      
 |      Returns the following sibling of this element or None.
 |  
 |  getparent(...)
 |      getparent(self)
 |      
 |      Returns the parent of this element or None for the root element.
 |  
 |  getprevious(...)
 |      getprevious(self)
 |      
 |      Returns the preceding sibling of this element or None.
 |  
 |  getroottree(...)
 |      getroottree(self)
 |      
 |      Return an ElementTree for the root node of the document that
 |      contains this element.
 |      
 |      This is the same as following element.getparent() up the tree until it
 |      returns None (for the root element) and then build an ElementTree for
 |      the last parent that was returned.
 |  
 |  index(...)
 |      index(self, child, start=None, stop=None)
 |      
 |      Find the position of the child within the parent.
 |      
 |      This method is not part of the original ElementTree API.
 |  
 |  insert(...)
 |      insert(self, index, element)
 |      
 |      Inserts a subelement at the given position in this element
 |  
 |  items(...)
 |      items(self)
 |      
 |      Gets element attributes, as a sequence. The attributes are returned in
 |      an arbitrary order.
 |  
 |  iter(...)
 |      iter(self, tag=None)
 |      
 |      Iterate over all elements in the subtree in document order (depth
 |      first pre-order), starting with this element.
 |      
 |      Can be restricted to find only elements with a specific tag
 |      (pass ``tag="xyz"``) or from a namespace (pass ``tag="{ns}*"``).
 |      
 |      You can also pass the Element, Comment, ProcessingInstruction and
 |      Entity factory functions to look only for the specific element type.
 |  
 |  iterancestors(...)
 |      iterancestors(self, tag=None)
 |      
 |      Iterate over the ancestors of this element (from parent to parent).
 |      
 |      The generated elements can be restricted to a specific tag name with
 |      the 'tag' keyword.
 |  
 |  iterchildren(...)
 |      iterchildren(self, tag=None, reversed=False)
 |      
 |      Iterate over the children of this element.
 |      
 |      As opposed to using normal iteration on this element, the generated
 |      elements can be restricted to a specific tag name with the 'tag'
 |      keyword and reversed with the 'reversed' keyword.
 |  
 |  iterdescendants(...)
 |      iterdescendants(self, tag=None)
 |      
 |      Iterate over the descendants of this element in document order.
 |      
 |      As opposed to ``el.iter()``, this iterator does not yield the element
 |      itself.  The generated elements can be restricted to a specific tag
 |      name with the 'tag' keyword.
 |  
 |  iterfind(...)
 |      iterfind(self, path, namespaces=None)
 |      
 |      Iterates over all matching subelements, by tag name or path.
 |      
 |      The optional ``namespaces`` argument accepts a
 |      prefix-to-namespace mapping that allows the usage of XPath
 |      prefixes in the path expression.
 |  
 |  itersiblings(...)
 |      itersiblings(self, tag=None, preceding=False)
 |      
 |      Iterate over the following or preceding siblings of this element.
 |      
 |      The direction is determined by the 'preceding' keyword which
 |      defaults to False, i.e. forward iteration over the following
 |      siblings.  When True, the iterator yields the preceding
 |      siblings in reverse document order, i.e. starting right before
 |      the current element and going left.  The generated elements
 |      can be restricted to a specific tag name with the 'tag'
 |      keyword.
 |  
 |  itertext(...)
 |      itertext(self, tag=None, with_tail=True)
 |      
 |      Iterates over the text content of a subtree.
 |      
 |      You can pass the ``tag`` keyword argument to restrict text content to
 |      a specific tag name.
 |      
 |      You can set the ``with_tail`` keyword argument to ``False`` to skip
 |      over tail text.
 |  
 |  keys(...)
 |      keys(self)
 |      
 |      Gets a list of attribute names.  The names are returned in an
 |      arbitrary order (just like for an ordinary Python dictionary).
 |  
 |  makeelement(...)
 |      makeelement(self, _tag, attrib=None, nsmap=None, **_extra)
 |      
 |      Creates a new element associated with the same document.
 |  
 |  remove(...)
 |      remove(self, element)
 |      
 |      Removes a matching subelement. Unlike the find methods, this
 |      method compares elements based on identity, not on tag value
 |      or contents.
 |  
 |  replace(...)
 |      replace(self, old_element, new_element)
 |      
 |      Replaces a subelement with the element passed as second argument.
 |  
 |  set(...)
 |      set(self, key, value)
 |      
 |      Sets an element attribute.
 |  
 |  values(...)
 |      values(self)
 |      
 |      Gets element attribute values as a sequence of strings.  The
 |      attributes are returned in an arbitrary order.
 |  
 |  xpath(...)
 |      xpath(self, _path, namespaces=None, extensions=None, smart_strings=True, **_variables)
 |      
 |      Evaluate an xpath expression using the element as context node.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  attrib
 |      Element attribute dictionary. Where possible, use get(), set(),
 |      keys(), values() and items() to access element attributes.
 |  
 |  base
 |      The base URI of the Element (xml:base or HTML base URL).
 |      None if the base URI is unknown.
 |      
 |      Note that the value depends on the URL of the document that
 |      holds the Element if there is no xml:base attribute on the
 |      Element or its ancestors.
 |      
 |      Setting this property will set an xml:base attribute on the
 |      Element, regardless of the document type (XML or HTML).
 |  
 |  nsmap
 |      Namespace prefix->URI mapping known in the context of this
 |      Element.  This includes all namespace declarations of the
 |      parents.
 |      
 |      Note that changing the returned dict has no effect on the Element.
 |  
 |  prefix
 |      Namespace prefix or None.
 |  
 |  sourceline
 |      Original line number as found by the parser or None if unknown.
 |  
 |  tag
 |      Element tag
 |  
 |  tail
 |      Text after this element's end tag, but before the next sibling
 |      element's start tag. This is either a string or the value None, if
 |      there was no text.
 |  
 |  text
 |      Text before the first subelement. This is either a string or 
 |      the value None, if there was no text.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T

[Finished in 1.5s]